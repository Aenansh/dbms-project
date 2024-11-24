document.getElementById('bookingForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const data = {
      Student_ID: document.getElementById('student_id').value,
      No_of_People: document.getElementById('no_of_people').value,
      Pickup_Location: document.getElementById('pickup_location').value,
      Drop_Location: document.getElementById('drop_location').value,
      Time: document.getElementById('time').value,
      Car_Type: document.getElementById('car_type').value,
      Day: document.getElementById('day').value
  };

  fetch('/book_taxi', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => alert(data.message))
  .catch(error => console.error('Error:', error));
});
