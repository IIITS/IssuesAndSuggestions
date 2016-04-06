$(document).ready(function(){
window.upvote =function(CID){
	$.ajax({
		url: '/upvote/complaint',
		method: 'GET',
		data:{
			"ID" : CID,
			"status":$("#upvote-"+CID).attr('data-upvoted');
			
		},
		success:function(data){
			datalist = data.split(',');
			alert(datalist[0]);
			document.getElementById('upvote-container-'+CID).innerHTML=datalist[1];
			if(datalist[0] == "200"){
				$('#upvote-symbol-o-'+CID).removeClass("fa-thumbs-o-up").addClass("fa-thumbs-up");
			}
			else if(datalist[0] == "300"){
				$('#upvote-symbol-o-'+CID).removeClass("fa-thumbs-up").addClass("fa-thumbs-o-up");
			}
			
		}
		
	});
}

window.formSuggestionSubmit = function(CID){
	$.ajax({
		url: '/submit/suggestion/',
		method: 'GET',
		data:{
			"ID" : CID,
			"suggestion":""
		},
		success:function(data){
			datalist = data.split(',');
			alert(datalist[0]);
			$('#numupvotes-'+CID).html(datalist[1]);
		}
		
	});
}

});


