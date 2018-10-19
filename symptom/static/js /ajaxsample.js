// ajaxsample.js를 정의해서 static으로 import하면 html이 안먹는 현상 발생

$(document).ready(function(){

    $(".like").click(function(){

        $.ajax({ // .like 버튼을 클릭하면 <새로고침> 없이 ajax로 서버와 통신하겠다.
        type: "POST", // 데이터를 전송하는 방법을 지정
        url: "http://127.0.0.1:8000/ajaxtest/", // 통신할 url을 지정
        data: {'data': 1, 'csrfmiddlewaretoken': '{{ csrf_token }}'}, // 서버로 데이터 전송시 옵션
        dataType: "json", // 서버측에서 전송한 데이터를 어떤 형식의 데이터로서 해석할 것인가를 지정, 없으면 알아서 판단
        
        // 서버측에서 전송한 Response 데이터 형식 (json)
        // {'likes_count': post.like_count, 'message': message }
        });
    });
});