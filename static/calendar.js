function setNewMonth(direction) {
    const urlParams = new URLSearchParams(window.location.search);
    let currentMonth = urlParams.get('month') ? parseInt(urlParams.get('month')) - 1 : new Date().getMonth(); 
    let currentYear = urlParams.get('year') ? parseInt(urlParams.get('year')) : new Date().getFullYear();

    if (direction === 1) {
        if (currentMonth === 11) {
            currentMonth = 0;
            currentYear += 1;
        } else {
            currentMonth += 1;
        }
    } else if (direction === -1) {
        if (currentMonth === 0) {
            currentMonth = 11;
            currentYear -= 1;
        } else {
            currentMonth -= 1;
        }
    }

    urlParams.set('month', currentMonth + 1); // Convert back to 1-based month
    urlParams.set('year', currentYear);
    window.location.search = urlParams.toString();
}

function setSelectedDay() {
    const urlParams = new URLSearchParams(window.location.search);
}

(function() {
    window.store = {}

    const previous = document.querySelector('.mantiplex-previous-month');
    previous.addEventListener('click', function() {
        setNewMonth(-1);
    });
    const next = document.querySelector('.mantiplex-next-month');
    next.addEventListener('click', function() {
        setNewMonth(1);
    });
    const selectedDays = document.querySelectorAll('.mantiplex-calendar-day');
    for (const element of selectedDays) {
        element.addEventListener('click', function(e) {
            window.store.selectedDay = e.target.dataset.selectedDay;
            window.store.selectedMonth = e.target.dataset.selectedMonth;
            setSelectedDay();
        });
    }
})();