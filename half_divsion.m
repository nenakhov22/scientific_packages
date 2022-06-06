clear
a = 0; b = 14;
x = linspace(a,b,500)
h = 0.001; iter=1000; eps=0.001;
f=@(x)sin(x)./x;
y=f(x);
plot(x,f(x),x,0*x,':'); grid on
xlabel('x'); ylabel('y')
hold on
ymin=min(y); ymax=max(y);
if ymin<0 ymin=1.1*ymin; else ymin=0.9*ymin; end;
if ymax>0 ymax=1.1*ymax; else ymax=0.9*ymax; end;
axis([a,b,ymin,ymax]);
z = ginput(2); z1=z(1,1), z2=z(2,1);
f1 = f(z1); f2=f(z2); z=(z1+z2)/2; y=f(z);
flag = 0;
if f1*f2>0 'Плохие точки'
end;
for i=1:iter
    z=(z1+z2)/2; y=f(z);
    if y*f1<0
        z2=z;
    else z1=z;
    end;
    if abs(f(z))<eps
        flag = 1;
        break;
    end;
end;
if flag == 1
    plot(z1,0,'*',z2,0,'*',z,0,'o');
    disp("Найденный корень " + z);
end;
hold off
