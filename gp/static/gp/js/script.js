$(document).ready(function(){
window.upvote =function(CID){
	$.ajax({
		url: '/upvote/complaint/',
		method: 'GET',
		data:{
			"ID" : CID,
			"status":$("#upvote-"+CID).attr('class')
			
		},
		success:function(data){
			datalist = data.split(',');
			
			document.getElementById('upvote-container-'+CID).innerHTML=datalist[1];
			console.log(datalist[1]);
			console.log(datalist);
			if(datalist[0] == "upvoted"){
				$('#upvote-symbol-o-'+CID).removeClass("fa-thumbs-o-up").addClass("fa-thumbs-up");
				$("#upvote-"+CID).removeClass("not-upvoted").addClass("upvoted");

			}
			else if(datalist[0] == "not-upvoted"){
				$('#upvote-symbol-o-'+CID).removeClass("fa-thumbs-up").addClass("fa-thumbs-o-up");
				$("#upvote-"+CID).removeClass("upvoted").addClass("not-upvoted");
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


