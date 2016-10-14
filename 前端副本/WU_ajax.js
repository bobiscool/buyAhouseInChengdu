/**
 * Created by mac on 16/8/29. 邬一平自制的ajax:)
 */
function F_ajax(url,F_sucucess,F_failed) {
    //创建ajax 对象
    var a =0;
    if (window.XMLHttpRequest) {  //z这样 IE下没有这东西   应用 会报错
         var O_ajax = new XMLHttpRequest();
    } else {
         var O_ajax = new ActiveXObject();
    }

    console.log(O_ajax);

    //连接服务器 open(方法,文件名,'异步传输')
    //js 里面 同步 事情一件一件来    异步  就是独立来
    O_ajax.open('GET', url+'?t=' + new Date().getTime(), true);

    //第三步 发动请求
    O_ajax.send();

    //第四步  接受返回
    O_ajax.onreadystatechange = function () {
        if (O_ajax.readyState == 4) { //读取完成  无论 成功失败 都会完成
            if (O_ajax.status == 200) { //http状态码
                //console.log('OK'+O_ajax.responseText)
                F_sucucess(O_ajax.responseText);
                a=O_ajax.responseText;
            } else {
                F_failed?F_failed(O_ajax.status):alert("数据获取失败了，请尝试刷新"+O_ajax.status);
            }


        }

        /**
         * 0 代表 刚创建 ajax对象
         * 1  已经调用完send方法的时候
         * 2  代表载入完成 已收到全部响应内容 (可能加密了)
         * 3  解析响应内容
         * 4  级戏完毕 可以用于客户端调用
         */
        return a;
    }

}
