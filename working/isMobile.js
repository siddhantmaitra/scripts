// To detect client-side if the user is on a non-desktop device

function isMobile() {
    if (navigator.userAgentData != undefined) {
    if (navigator.userAgentData.mobile) {
      console.log("userAgentData mobile device");
    } else {
      console.log("userAgentData desktop device");
    }
  }
  if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    console.log("UA-regex mobile device");
  } else {
    console.log("UA-regex desktop device");
  }

  if (window.matchMedia("(max-width: 767px)").matches) {
    console.log("mq mobile device");
  } else {
    console.log("mq desktop device");
  }

}

isMobile();
