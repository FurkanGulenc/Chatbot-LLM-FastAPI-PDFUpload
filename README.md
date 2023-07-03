
1) Endpointlerden biri multipart/form-data kabul edecektir. Bir “pdf” dosya upload edilecektir.

2) Upload işleminden sonra bu enpoint upload edilen pdf dosyayı parçalara ayırıp, bu parçaları embed edip, persist olarak bir vector db de saklayacaktır. 2. Ve 3. Adımdan sonra bu endpoint in işlemi bitmiş olacak kullanıcıya json olarak bir sonuç dönecektir.

3) Bir diğer endpoint ise kullanıcıdan sadece bir soru alacaktır json body olarak. Bu soruyu embed ederek, vector db den similarity search yapacaktır. Bu search sonucunda gelen parçalarla beraber kullanıcı sorusunu open ai ın ilgili endpoint ine soru olarak soracaktır, ve sonucu json olarak geri dönecektir.
