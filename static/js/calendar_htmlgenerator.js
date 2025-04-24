(function() {
    const selectedDay = document.querySelectorAll('.events');
    for (const element of selectedDay) {
        element.addEventListener('click', function(e) {
            axios.get('event/list', {
                params: {
                    selected_date: e.target.dataset.selectedDate
                }})
            .then(response => {
                console.log(response.data.events)
                const eventsContainer = document.getElementsByClassName('events-container');
                const events = response.data.events || [];
                const tasksContainer = document.getElementById('tasks-container');
                const tasks = response.data.tasks || [];

                if (events.length > 0) {
                    eventsContainer.innerHTML = events.map(event =>
                        `<div class="list-group">
                        <a class="list-group-item list-group-item-action">
                            <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">${event.name || 'No data'}</h5>
                            <small>${event.begin_time || 'No data'} - ${event.end_time || 'No data'}</small>
                            </div>
                        </a>
                        </div>
                        `).join('');
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
                        `<div class="list-group">
                        <a class="list-group-item list-group-item-action">
                            <div class="d-flex w-100 justify-content-between">
                            <h5 class="mb-1">${task.name || 'No data'}</h5>
                            </div>
                        </a>
                        </div>
                        `).join('');
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
})