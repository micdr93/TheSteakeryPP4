$(document).ready(function () {
    const openingHours = {
        0: { open: "11:00", close: "21:00" },  // Sunday
        1: { open: "12:00", close: "22:00" },  // Monday
        2: { open: "12:00", close: "22:00" },  // Tuesday
        3: { open: "12:00", close: "22:00" },  // Wednesday
        4: { open: "12:00", close: "22:00" },  // Thursday
        5: { open: "12:00", close: "23:00" },  // Friday
        6: { open: "12:00", close: "23:00" }   // Saturday
    };

    const brunchEnd = "15:00"; // Brunch ends at 3 PM on Sundays

    $('#date').on('change', function () {
        const selectedDate = new Date($(this).val());
        const day = selectedDate.getDay(); // Get day of the week (0 = Sunday, 1 = Monday, etc.)
        const hours = openingHours[day];

        $('#time').attr('min', hours.open);
        $('#time').attr('max', hours.close);

        // Special case for Sunday brunch
        if (day === 0 && selectedDate.getHours() < 15) {
            $('#time').attr('min', "11:00");
            $('#time').attr('max', brunchEnd);
        }
    });

    $('#reservationForm').on('submit', function (e) {
        e.preventDefault();

        const date = $('#date').val();
        const time = $('#time').val();
        const guests = parseInt($('#guests').val());
        const phone = $('#phone').val();
        const email = $('#email').val();
        const tableId = parseInt($('#table').val());

        // Include CSRF token in AJAX request
        const csrftoken = getCookie('csrftoken');

        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: {
                date: date,
                time: time,
                guests: guests,
                phone: phone,
                email: email,
                table: tableId
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function (response) {
                alert('Booking successfully made!');
            },
            error: function (xhr, errmsg, err) {
                alert('An error occurred: ' + errmsg);
            }
        });
    });

    // Utility function to get the CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
