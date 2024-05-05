const darkModeToggle = document.getElementById('dark-mode-toggle');
const body = document.body;

darkModeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
});

// Add hover animation to pricing columns
document.querySelectorAll('.pricing-column').forEach((column) => {
    column.addEventListener('mouseover', () => {
        column.classList.add('hover');
    });
    column.addEventListener('mouseout', () => {
        column.classList.remove('hover');
    });
});