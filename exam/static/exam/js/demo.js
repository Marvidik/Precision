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
    var info=deocument.getElementById("mod");
    
    for (i = 0; i < e.length; i++) {
        if (e[i].type == "radio") {
        if (e[i].checked) {
            var choice=e[i]
            var m=( "Q" + choice.name + "Answer you selected is :" + choice.value + "<br/>");
            info.innerHTML=m
             
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
    document.getElementById("escore").value=tscore;
    
    }
