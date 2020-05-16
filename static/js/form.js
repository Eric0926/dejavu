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
				$('#successAlert').text(data[0].img0).show();
				$('#img2').attr("src", data[0].img1);
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});
