$(function(){
	$('#PM-table').hide();
    $('#VM-table').show();
	$('#VMinput').click(function(){
		//console.info("VMinput");
		$('#PM-table').hide();
        $('#VM-table').show();
	});
	$('#PMinput').click(function(){
		//console.info("PMinput");
		$('#VM-table').hide();
        $('#PM-table').show();
	});
});