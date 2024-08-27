<h2>USB Cihaz ve Soket Sunucusu </h2>

<p>
    Bu proje, iki farklı sunucudan oluşmaktadır: <strong>USB Cihaz Sunucusu</strong> ve <strong>Soket Sunucusu</strong>. 
    USB Cihaz Sunucusu, sisteme takılan USB cihazlarını takip etmek ve bu cihazlara yönelik belirli işlemleri gerçekleştirmek için kullanılır. 
    Soket Sunucusu ise belirtilen bir port üzerinden gelen istemci bağlantılarını dinleyerek veri alışverişi yapar.
</p>

<h2>USB Cihaz Sunucusu</h2>
<p>
    Linux sistemine bağlanan USB cihazlarını izlemek ve gerçek zamanlı bildirimler sağlamak için tasarlanmıştır. 
    Bir USB cihazı bağlandığında veya çıkarıldığında, sunucu <code>notify-send</code> kullanarak bildirim gönderebilir. 
    Sunucu, sistem düzeyinde görevler için verimli olmasını sağlayan bir <code>systemd</code> hizmeti olarak yapılandırılmıştır. 
    Sunucu, dosya sistemi türü, etiket, UUID, bağlama noktası ve bağlantı durumu gibi cihaz bilgilerini yakalar ve bu bilgileri bir istemciye ileterek işlenmesini veya kaydedilmesini sağlar.
</p>

<h2>Soket Sunucusu</h2>
<p>
    Soket Sunucusu, belirli bir portta gelen istemci bağlantılarını dinleyen basit bir TCP sunucusudur. 
    JSON formatında veri göndermek ve almak için kullanılabilir, bu da yapılandırılmış veri alışverişi gerektiren uygulamalar için uygundur. 
    Sunucu, <code>systemd</code> ile yönetilir, bu sayede kolayca başlatılabilir, durdurulabilir ve izlenebilir. 
    İstemciler bu sunucuya bağlanarak JSON verilerini gönderebilir ve yanıt alabilir.
</p>
