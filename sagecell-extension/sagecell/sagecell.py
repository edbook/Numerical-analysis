#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive



class sagecell(nodes.General, nodes.Element): 
    pass


def html_visit_sagecell_node(self, node):
    # the code is either in R or Sage
    if node["r"]:
        self.body.append("<div class='rsage'>")
    else:
        self.body.append("<div class='sage'>")

    self.body.append("<script type='text/x-sage'>")	    
    self.body.append(node['code'])    
    self.body.append("</script>")    
    self.body.append("</div>")	


def html_depart_sagecell_node(self, node):
    pass


def latex_visit_sagecell_node(self, node):
    # If "showcode" is True the code is displayed verbatim, 
    # Then an image of the outcome isi displayed if an image file was given.
    if node["showcode"]:
        self.body.append("\n\n")
        self.body.append("\\begin{verbatim}\n")
        self.body.append(node['code'])
        self.body.append("\n\end{verbatim}")
        self.body.append("\n\n")

    if node["img"] != None:
        self.body.append("\n\n")
        self.body.append("\\begin{center}\n")
        self.body.append("\\includegraphics[width="+node['imgwidth']+",keepaspectratio=true]{"+node['img']+"}\n")
        self.body.append("\n\end{center}")

def latex_depart_sagecell_node(self, node):
    pass


class SageCell(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 5
    option_spec = {
        "codefile": directives.unchanged,
        "r": directives.unchanged,
        "showcode": directives.unchanged,
        "img": directives.unchanged,
        "imgwidth": directives.unchanged,
    }
	
    def run(self):              
 
        if "codefile" in self.options:
            codefile = self.options.get("codefile")
            f = open(codefile,'r')
            code = f.read()
        else:
            code = '\n'.join(self.content)

        if "r" in self.options:
            r = True
        else: 
            r = False

        if "showcode" in self.options:
            showcode = True
        else: 
            showcode = False

        if "img" in self.options:
            img = self.options.get("img")
        else:
            img = None

        if "imgwidth" in self.options:
            imgwidth = self.options.get("imgwidth")
        else:
            imgwidth = "8cm"

        content_list = self.content

        node = sagecell()  
        node['code'] = code     
        node['r'] = r  
        node['showcode'] = showcode
        node['img'] = img
        node['imgwidth'] = imgwidth
    
        return [node]		


def setup(app):
    app.add_node(sagecell, html = (html_visit_sagecell_node, html_depart_sagecell_node), latex = (latex_visit_sagecell_node, latex_depart_sagecell_node))
    app.add_directive("sagecell", SageCell)



