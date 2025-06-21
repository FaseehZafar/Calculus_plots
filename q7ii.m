% Function ii: f(x) = cos²x - 2sinx
f2 = @(x) (cos(x)).^2 - 2*sin(x);

% Plot over [0,2π]
x2 = linspace(0, 2*pi, 500);
figure(2);
plot(x2, f2(x2), 'r-', 'LineWidth', 2);
xlabel('x'); ylabel('f(x)');
title('f(x) = cos^2x - 2sinx'); grid on;
xticks(0:pi/2:2*pi);
xticklabels({'0','π/2','π','3π/2','2π'});

% Find critical points
f2_sym = (cos(x))^2 - 2*sin(x);
df2 = diff(f2_sym);
crit2 = solve(df2 == 0, x);
crit2 = double(crit2(crit2 >= 0 & crit2 <= 2*pi));
disp('Critical points for f(x)=cos²x-2sinx in [0,2π]:');
disp(crit2');
