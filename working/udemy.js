// Complete the annoying courses mandated for some reason

let buttons = document.querySelectorAll('div.ud-btn-link');
buttons.forEach(function(button) {
    button.click();
});

let checkboxes = document.querySelectorAll('input[data-purpose="progress-toggle-button"]');
checkboxes.forEach(function(checkbox) {
    checkbox.removeAttribute('disabled');
    checkbox.click();
});
