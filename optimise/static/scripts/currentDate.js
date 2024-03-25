document.addEventListener('DOMContentLoaded', function() {
    var currentDateElement = document.getElementById('currentDate');
    var currentDate = new Date();

    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    var formattedDate = currentDate.toLocaleDateString('en-US', options);

    // currentDateElement.textContent = 'Today is: ' + formattedDate;
    currentDateElement.textContent = formattedDate;
});
