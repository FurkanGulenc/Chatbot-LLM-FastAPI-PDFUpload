Tamamlamanız istenen case in gene mimari çizimi ektedir. Detayları aşağıdaki gibi olacaktır;

1. Fast Api ile kullanarak bir API projesi hazırlamanız gerekmektedir. İki adet endpoint e sahip olması yeterlidir. Bu endpointler postman ile denenecektir. Bu api projesine gerekli dockerfile ve docker-compose dosyalarını ekleyip “docker-compose up --build” komutu ile ayağa kaldırılabiliyor olmak ek puan kazandıracaktır.

2) Endpointlerden biri multipart/form-data kabul edecektir. Bir “pdf” dosya upload edilecektir.

3. Upload işleminden sonra bu enpoint upload edilen pdf dosyayı parçalara ayırıp, bu parçaları embed edip, persist olarak bir vector db de saklayacaktır. 2. Ve 3. Adımdan sonra bu endpoint in işlemi bitmiş olacak kullanıcıya json olarak bir sonuç dönecektir.

4) Bir diğer endpoint ise kullanıcıdan sadece bir soru alacaktır json body olarak. Bu soruyu embed ederek, vector db den similarity search yapacaktır. Bu search sonucunda gelen parçalarla beraber kullanıcı sorusunu open ai ın ilgili endpoint ine soru olarak soracaktır, ve sonucu json olarak geri dönecektir.

Not 1: request ve response modellere istediğiniz gibi karar verebilirsiniz.

Not 2: İstek zormuş gibi görünse de sizlere çok büyük kolaylık sağlaaycak olan “langchain” kütüphanesini kullanmanız gerekmektedir. (https://python.langchain.com/docs/get_started/quickstart

Quickstart | 🦜️🔗 Langchain
Installation
python.langchain.com
)

Not 3: Langchain kütüphanesinde, “Documen Loader”, “VectorStores”, “Conversational Retrieval QA Chain” gibi bölümler sizlere çok yardımcı olacaktır. Vector store olarak kendi lokalinizde Chroma yada cloud da hesap açarak pinecone vs kullanabilirsiniz, bu tercih size kalmış.

Not 4: Open AI ı api olarak kullanmanız için aşağıdaki OPEN_AI_API_KEY i kullanabilirsiniz. Bu key Haftaya Pazartesi dispose olacaktır.

“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”

Başka bir sorunuz olduğunda bizimle iletişime geçebilirsiniz.
