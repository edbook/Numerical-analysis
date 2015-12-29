# Benedikt Magnusson, 2015. CC-BY-SA.
# Addapted from a version of William Stein, 
# http://wiki.sagemath.org/interact/calculus#Root_Finding_Using_Bisection
def newton_method(f, c, eps, maxiter=100):
    x = f.variables()[0]
    fprime = f.derivative(x)
    try:
        g = f._fast_float_(x)
        gprime = fprime._fast_float_(x)
    except AttributeError:
        g = f; gprime = fprime
    iterates = [c]
    for i in xrange(maxiter):
       fc = g(c)
       if abs(fc) < eps: return c, iterates
       c = c - fc/gprime(c)
       iterates.append(c)
    return c, iterates
    
var('x')    
#html("<h1>Double Precision Root Finding Using Newton's Method</h1>")
@interact
def _(f = x^2 - 2, c = float(0.5), eps=(-3,(-16..-1)), interval=float(0.5)):
     eps = 10^(eps)
     print "eps = %s"%float(eps)
     z, iterates = newton_method(f, c, eps)
     print "root =", z
     print "f(c) = %r"%f(x=z)
     n = len(iterates)
     print "iterations =", n
     html(iterates)
     P = plot(f, (x,z-interval, z+interval), rgbcolor='blue')
     h = P.ymax(); j = P.ymin()
     L = sum(point((w,(n-1-float(i))/n*h), rgbcolor=(float(i)/n,0.2,0.3), pointsize=10) + \
             line([(w,h),(w,j)],rgbcolor='black',thickness=0.2) for i,w in enumerate(iterates))
     show(P + L, xmin=z-interval, xmax=z+interval)

show(html("<a rel='license' href='http://creativecommons.org/licenses/by-sa/3.0/'><img alt='Creative Commons License' style='border-width:0' src='https://i.creativecommons.org/l/by-sa/3.0/80x15.png' /></a> by <a href='http://wiki.sagemath.org/interact/calculus#Newton.27s_Method'>William Stein</a>"))

