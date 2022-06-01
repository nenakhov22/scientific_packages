n = 4*pi;
t1 = pi*(-n:n)/n;
t2 = pi/2*(-n:n)'/n;
x = cos(t2)*cos(t1);
y = cos(t2)*sin(t1);

z = sin(t2);
plot3(x,y,z);
clear all
t = -5*pi:pi/250:5*pi;
x = (cos(2*t).^2).*sin(t);
y = (sin(2*t).^2).*cos(t);
comet3(x,y,t);
[x,y]=meshgrid(-5:0.1:5,-5:0.1:5);
plot(x,y);
x = -10:0.5:10;
y = -10:0.5:10;
[X,Y] = meshgrid(x,y);
Z = sin(sqrt(X.^2+Y.^2))./sqrt(sqrt(X.^2+Y.^2));
surfc(X,Y,Z)
xlabel('x')
ylabel('y')
zlabel('z')
x = linspace(-2,0,20)
[X,Y]= meshgrid(x,-x);
Z = 2./exp((X-.5).^2+Y.^2)-2./exp((X+0.5).^2+Y.^2)
subplot(2,2,1)
surf(X,Y,Z);
shading faceted;
title('shading faceted')
subplot(2,2,2)
surf(X,Y,Z);
shading flat;
title('shading flat')
subplot(2,2,3)
surf(X,Y,Z);
shading interp;
title('shading interp')
[X,Y] = meshgrid(-1:.1:1,-1:.1:1);
Z = sin(X).*cos(Y)
contour(X,Y,Z,10)
  
F = @(x,y)(x.^2+y.^2).^2
fsurf(F,[-pi,pi,-pi,pi])
fx = @(u,v)u.*cos(v);
fy = @(u,v)u.*sin(v);
fz = @(u,v)u.^4;
fsurf(fx,fy,fz, [-pi,pi,-pi,pi])
