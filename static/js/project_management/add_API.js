     // 修改表单
    function del(id,name,host,decs){
        // {#/* 显示弹窗 */#}
        document.getElementById("delete").style.display="block";
        // {# 弹窗标题 #}
        document.getElementById("popup_title").innerText = '修改Host';
        // {# 绑定当前弹窗表单里面id值 #}
         document.getElementById("ids").value = id
        // {# 自动填充name、host、描述 #}
        document.getElementById("name").value = name
        document.getElementById("host").value = host
        document.getElementById("description").value = decs
        // {# 给form表单传个接口地址 #}
        document.getElementById("popup_form").action = 'http://127.0.0.2:8005/project/host/update';

    }
    // {# 新增表单 #}
    function add() {
        // init重置表单所有控件为空
        document.getElementById("ids").value = '';
        document.getElementById("name").value = '';
        document.getElementById("host").value = '';
        document.getElementById("description").value = '';

        document.getElementById("delete").style.display="block";
        // 传递接口链接
        document.getElementById("popup_form").action = 'http://127.0.0.2:8005/project/host/insert';
        // 修改表单名字
        document.getElementById("popup_title").innerText = '新增Host';

    }

    function delesc(){
        // {#/* 编辑host表单点击取消时隐藏弹窗 */#}
        document.getElementById("delete").style.display="none";
    }

    // {# 删除host #}
    function http_delete(id) {
        // {#/* 发送请求删除host,判断确认删除框，为false不删除，为true执行删除 */#}
        if (!confirm("确认要删除？")) {
            window.event.returnValue = false;
        } else {
            const Http = new XMLHttpRequest();
            const url = "http://127.0.0.2:8005/project/host/delete?id=" + id;
            Http.open('get', url);
            Http.send();
        }

    }

