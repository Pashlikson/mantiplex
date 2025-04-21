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

    urlParams.set('month', currentMonth + 1);
    urlParams.set('year', currentYear);
    window.location.search = urlParams.toString();
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
    const selectedDay = document.querySelectorAll('.events');
    for (const element of selectedDay) {
        element.addEventListener('click', function(e) {
            console.log('Selected day:', e.target.dataset.selectedDate);
            axios.get('event/list', {
                params: {
                    selected_date: e.target.dataset.selectedDate
                }})
            .then(response => {
                const eventsContainer = document.getElementById('events-container');
                const events = response.data.events || [];
                const tasksContainer = document.getElementById('tasks-container');
                const tasks = response.data.tasks || [];
                
                if (events.length > 0) {
                    eventsContainer.innerHTML = events.map(event => 
                        `
                        <div class="list-group">
                        <a class="list-group-item list-group-item-action">
                            <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">${event.name || 'No data'}</h5>
                            <small>${event.begin_time || 'No data'} - ${event.end_time || 'No data'}</small>
                            </div>
                            <p class="mb-1">${event.context || 'No data'}</p>
                            <p class="mb-1">${event.event_adress || 'No data'}</p>
                            <small>${event.event_status || 'No data'}</small>
                        </a>
                        </div>
                        `).join('');
                    console.log('Events container:', eventsContainer.innerHTML);
                    }
                else {
                    eventsContainer.innerHTML = `<div class="list-group">
                            <a class="list-group-item list-group-item-action">
                                <p>No events found for this date.</p>
                            </a>
                            </div>`;
                }
                
                if (tasks.length > 0) {
                    tasksContainer.innerHTML = tasks.map(task => 
                        `
                        <div class="list-group">
                        <a class="list-group-item list-group-item-action">
                            <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">${task.name || 'No data'}</h5>
                            <small>${task.begin_time || 'No data'} - ${task.end_time || 'No data'}</small>
                            </div>
                            <p class="mb-1">${task.context || 'No data'}</p>
                            <small>${task.status || 'No data'}</small>
                        </a>
                        </div>
                        `).join('');
                    console.log('Events container:', tasksContainer.innerHTML);
                    }
                else {
                    tasksContainer.innerHTML = `<div class="list-group">
                            <a class="list-group-item list-group-item-action">
                                <p>No tasks found for this date.</p>
                            </a>
                            </div>`;
                }
            })
            .catch(error => {
                console.error('Error fetching events:', error);
            });
            });
        }
})();