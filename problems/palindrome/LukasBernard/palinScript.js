$(document).ready(
	function() 
	{
    	$('#palindromeForm').on('submit', function(e) 
		{
        	e.preventDefault();
        	$.ajax(
				{
					url: '/process',
					type: 'POST',
					data: {input_String: $('#inputString').val()},
					success: function(response) 
					{
						$('#response').text(response);
					},
					error: function(error) 
					{
						$('#response').text('Error: ' + error.statusText);
					}
        		});
    	});
	});

