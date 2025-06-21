% Define the simplified function: h(x) = x - 4x^(1/3)
h = @(x) x - 4*x.^(1/3);

% Create x values (-2 to 2)
x = -2:0.01:2;

% Basic plot
plot(x, h(x), 'b-')
grid on
title('h(x) = x - 4x^{1/3}')
xlabel('x'), ylabel('h(x)')

% Find critical point
crit_point = (4/3)^(3/2);  % Solved analytically
disp(['Critical point at x = ', num2str(crit_point)])

% Mark critical point
hold on
plot(crit_point, h(crit_point), 'ro')
legend('Function', 'Critical Point')
