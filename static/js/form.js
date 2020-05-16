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
				$('#img2').attr("src", "https://storage.googleapis.com/flagged_evaluation_images/444_10_r2.png");
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});
