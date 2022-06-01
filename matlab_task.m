a=0;
b=4*pi;
m=100;
x=linspace(a,b,m);
f='x.sin(x)-cos(x)';
plot(x,eval(f),x,0*x);
grid on;
xlabel('x');
ylabel('y');
z=ginput(1);
[zr,fr]=fzero(f,z(1));
hold on;
plot((zr,fr,'r*',z(1),z(2),'g');
hold off;
zr
fr
syms y;
Eq=y.*sin(y)-cos(y)==0;
j=vpasolve(Eq,y);
j
