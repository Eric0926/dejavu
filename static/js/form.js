$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#nameInput').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.results).show();
				$('#img1').attr("src", data.results[0]).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});