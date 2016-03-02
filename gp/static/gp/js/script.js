$(document).ready(function(){
window.upvote =function(CID){
	$.ajax({
		url: '/upvote/complaint',
		method: 'GET',
		data:{
			ID : CID,
			
		},
		success:function(data){
			datalist = data.split(',');
			alert(datalist[0]);
			$('#numupvotes-'+CID).html(datalist[1]);
		}
		
	});
}

});


