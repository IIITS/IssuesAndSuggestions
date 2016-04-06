$(document).ready(function(){
window.upvote =function(CID){
	$.ajax({
		url: '/upvote/complaint',
		method: 'GET',
		data:{
			"ID" : CID,
			
		},
		success:function(data){
			datalist = data.split(',');
			alert(datalist[0]);
			$('#numupvotes-'+CID).html(datalist[1]);
		}
		
	});
}
window.deupvote =function(CID){
	$.ajax({
		url: '/deupvote/complaint',
		method: 'GET',
		data:{
			"ID" : CID,
			
		},
		success:function(data){
			datalist = data.split(',');
			alert(datalist[0]);
			$('#numupvotes-'+CID).html(datalist[1]);
		}
		
	});
}
window.formSuggestionSubmit = function(CID){
	$.ajax({
		url: '/submit/suggestion/',
		method: 'GET',
		data:{
			"ID" : CID,
			"suggestion":
		},
		success:function(data){
			datalist = data.split(',');
			alert(datalist[0]);
			$('#numupvotes-'+CID).html(datalist[1]);
		}
		
	});
}

});


