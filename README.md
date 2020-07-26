let rt = detail.type;
if (rt === 'script' || rt === 'stylesheet' || rt === 'main_frame' || rt === 'sub_frame') {
  for (let i in val) {
    if (val[i].name.toLowerCase() === 'content-security-policy') {
      let s = val[i].value;
      s = s.replace(/googleapis\.com/g, '$& https://gapis.geekzu.org');
      s = s.replace(/google\.com/g, '$& https://recaptcha.net');
      s = s.replace(/gstatic\.com/g, '$& https://*.gstatic.cn');
      val[i].value = s;
      break;
    }
  }
}
