const url=window.location.href
$(document).ready(function(){
    $("#b1").click(function(){
        $(".rb").show();
        $(".rb").attr("diasabled",true)

    });
    });
    var tscore=0;
    function getanswer()
    {
        
    var e = document.getElementsByTagName('input');
    
    for (i = 0; i < e.length; i++) {
        if (e[i].type == "radio") {
        if (e[i].checked) {
            var choice=e[i]
            console.log( "Q" + choice.name + "Answer you selected is :" + choice.value + "<br/>");
             
        }
      
        }
        if (e[i].type=="checkbox"){
            var ansr=e[i]
            console.log( "Q" + ansr.name + "The answer is  :" + ansr.value + "<br/>");
            if (choice.value==ansr.value){
                tscore+=5;        
            }
            else{
                tscore+=0;
            }
        }
        
        
    }
    document.getElementById("mscore").value=tscore;
    
    }



    function dosomething(){
        console.log(tscore)
        $.ajax({

            type:"GET",
            url:`${url}get_score`,
            data:{"tscore":tscore},
            dataType:"json",
            success:function(response){
                console.log(response)
            },
            error:function(error){
                console.log(error)
            }
        })
    }
