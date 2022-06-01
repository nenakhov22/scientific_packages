task_1();

function [tt, to_break] = check_root(f, x, epsil)
    tt = f(x);
    to_break = false;
    if abs(tt) < epsil
        hold on
        plot(x, tt, 'g.', MarkerSize=20)
        hold off
        to_break = true;
    end
end

function task_2_newton()
    [x_, y, y1] = plot_task_2();
    max_iter = 40;
    h = 1e-6;
    while true
        z = ginput(1);
        x = z(1);
        x_sol = fzero(@bar, x);
        skip_zs = false;
        for j = 1:max_iter
            [tt, to_break] = check_root(@bar, x, 1e-10);
            if to_break
                break
            end
            x_next = x - h*tt/(bar(x + h) - tt);
            hold on
            plot([x, x_next], [tt, bar(x_next)], 'r')
            hold off
            if ~skip_zs
                z = ginput(1);
                if z(2) < 0
                    skip_zs = true;
                end
            end
            plot(x_, y, x_, y1, ':')
            x = x_next;
        end
        disp(abs(x_sol-x))
    end
end

function [x, y, y1] = plot_task_2()
    fr = 0;
    to = 7;
    x = linspace(fr, to, 1000);
    y = bar(x);
    y1 = 0*x;
    plot(x, y, x, y1, ':');
end

function task_2_bin_search()
    max_iter = 40;
    plot_task_2()
    to = 7;
    while true
        z = ginput(2);
        z = z(:, 1);
        if z(1) > to
            break
        end
        if bar(z(1)) * bar(z) > 0
            error('no');
        end
        if bar(z(1)) > 0
            z = z(end:-1:1);
        end
        x_sol = fzero(@bar, z(1));
        skip_zs = false;
        for j = 1:max_iter
            t = sum(z)/2;
            [tt, to_break] = check_root(@bar, t, 1e-10);
            if to_break
                break
            end
            if ~skip_zs
                z_ = ginput(1);
                if z_(2) < 0
                    skip_zs = true;
                end
            end
            z((tt > 0) + 1) = t;
            hold on
            plot(t, tt, 'ro')
            hold off
        end
        disp(abs(x_sol-t))
    end
end

function task_1()
    % c
    x = linspace(0, 4*pi, 1000);
    plot(x, foo(x), x, 0*x, ':');
    zr = zeros(1, 100)
    i = 1
    while true
        z = ginput(1);
        if z(1) > 4*pi
            break
        end
        zr(i) = fzero(@foo, z(1));
        i = i+1;
    end
    hold on
    plot(zr(1:i-1), foo(zr(1:i-1)), 'ro')
    hold off
end

function res = foo(x)
    res = x.*sin(x) - cos(x);
end

function res = bar(x)
    %res = 1 + (1+sin(x)-cos(x)).^2 - (sin(2*x)-cos(2*x)-.2).^2;
    res = sin(x)./x
    %res = 1+x.*sin(x)
end
