% Function i: f(x) = x*e^(2x)
f1 = @(x) x.*exp(2*x);

% Plot from x=-2 to x=1 (shows key behavior)
x1 = linspace(-2, 1, 500);
figure(1);
plot(x1, f1(x1), 'b-', 'LineWidth', 2);
xlabel('x'); ylabel('f(x)');
title('f(x) = xe^{2x}'); grid on;

% Find critical points
syms x;
f1_sym = x*exp(2*x);
df1 = diff(f1_sym);
crit1 = solve(df1 == 0, x);
disp('Critical point for f(x)=xe^{2x}:');
disp(double(crit1));
