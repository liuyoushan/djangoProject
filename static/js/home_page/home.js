var oBtn=document.getElementById("btn1");
oBtn.onclick=function(){
    var oDiv=document.getElementById("div1");
    close(oDiv.style.display)

    if(oDiv.style.display==="none"){
    oDiv.style.display="block";
    }
    else{
    oDiv.style.display="none";
    }
    };


//------------------------------
var lis=document.querySelectorAll("#example1 li");
var len=lis.length;
//切换页签样式：遍历li，给li绑定onclick事件
for(var i=0;i<len;i++){
    lis[i].onclick=function(){
        //切换页签样式↓
        for(var i=0;i<len;i++){
            if(lis[i]==this){//判断是否为当前对象
                lis[i].style.background="#f90";
                lis[i].querySelector("a").style.color="white";
            }else{
                lis[i].style.background="white";
                lis[i].querySelector("a").style.color="black";
            }
        }
    }
}

//------------------------------
if (document.getElementById){ //http://www.codefans.net
    document.write('<style type="text/css">\n')
    document.write('.submenu{display: none;}\n')
    document.write('</style>\n')
}

function SwitchMenu(obj){
    if(document.getElementById){
        var el = document.getElementById(obj);
        var ar = document.getElementById("masterdiv")
        if(el.style.display != "block"){ //DynamicDrive.com change
            for (var i=0; i<ar.length; i++){
                if (ar[i].className=="submenu") //DynamicDrive.com change
                ar[i].style.display = "none";
                
            }
                el.style.display = "block";
        }else{
            el.style.display = "none";
        }
    }
}


