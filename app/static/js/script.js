$(document).ready(function(){
	
	$('form').on('submit' , function(event){
			
		$.ajax({
			data : {
				input : $('#word').val()
			},
			type : 'POST',
			url : '/search'
		})
		.done(function(data) {
			if(data.empty)
			{
				$('#display').text(data.empty)
			}
			else
			{
				
				$('#display').text('Matches:' + data.matches)
				
			}
		});

		event.preventDefault()
	});
});
