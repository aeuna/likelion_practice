let lastDay = new Date(new Date() - 1000 * 60 * 60 * 24)
  .toISOString()
  .substring(0, 10);
let dateInput = document.querySelector('.todayDateInput');
dateInput.value = lastDay;
dateInput.setAttribute('max', lastDay);

let contentsBox = document.querySelector('.contents'); // 그냥 html에 있는 class contents div

let movieCodeObject = {};
let movieNameArray = [];
let movieCodeArray = [];
const key = '?key=6c0c06137f3cf333d4bde6dbc28d7bdc';

const clickedSearchBtn = async () => {
  await giveRankObject()
    .then((data) => {
      let DtYear = data.boxOfficeResult.showRange.substring(0, 4);
      let DtMonth = data.boxOfficeResult.showRange.substring(4, 6);
      let DtDate = data.boxOfficeResult.showRange.substring(6, 8);
      // 20200906~20200906 형태에서 원하는 부분만 잘랐어요
      // 더 간략하게 할 수 있을거 같은데 일단 이렇게!
      let dateTitle = document.createTextNode(
        `${DtYear}년 ${DtMonth}월 ${DtDate}일 박스 오피스`
      );
      //appenchild해주기 위해 textnode로 담아 주시고
      let titleBox = document.createElement('h1');
      // h1 태그도 하나 만들어주시고
      let createDiv = document.createElement('div');
      //div도 만들어주시고
      createDiv.classList.add('moviePackage');
      // 만든 div 클래스에 moviePackage 를 추가해 주시고
      contentsBox
        .appendChild(createDiv)
        .appendChild(titleBox)
        .appendChild(dateTitle);
      // contentsBox 속에 만든 div 그 속에 titleBox(h1 태그) h1태그 글자를 dateTitle로 해줍시다.
      for (let i = 0; i < 10; i++) {
        let movieRankJson = data.boxOfficeResult.dailyBoxOfficeList[i].movieNm;
        let movieCodeJson = data.boxOfficeResult.dailyBoxOfficeList[i].movieCd;

        let text = document.createTextNode(`${i + 1}위 ` + movieRankJson);
        let textBox = document.createElement('button');

        contentsBox
          .appendChild(createDiv)
          .appendChild(textBox)
          .appendChild(text);

        textBox.setAttribute('value', `${movieRankJson}`);
        textBox.setAttribute('onClick', 'ClickedMovieBtn(this);');

        movieNameArray[i] = `${movieRankJson}`;
        movieCodeArray[i] = `${movieCodeJson}`;
        movieCodeObject[movieNameArray[i]] = `${movieCodeArray[i]}`;
      }
      console.log(movieCodeObject);
    })
    .catch((error) => console.log(`에러 발생 ${error.name}:${error.message}`));
};

const giveRankObject = async () => {
  let date = document.todayDateForm.todayDateInput.value;
  let targetDate = date.replaceAll('-', '');
  console.log(targetDate);
  const key = '?key=6c0c06137f3cf333d4bde6dbc28d7bdc'; // api key를 가져왔습니다.
  let targetTodayDate = `&targetDt=${targetDate}`;
  const url =
    'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json' +
    key +
    targetTodayDate; // 검색할 json파일 url 입니다

  const response = await fetch(url);
  return await response.json(); // text, arrayBuffer, blob, json, formData 종류가 있어요
};

const showMeTheCode = async (clickedValue) => {
  let iWantedValue = clickedValue.value; //영화이름
  let code = await movieCodeObject(iWantedValue); //영화이름에 해당하는 value를 반환
  let moreInfo = await searchMoreInfo(code);
  return await moreInfo;
};

const CodeInMovieObj = async (clickedValue) => {
  let iWantedValue = movieCodeObject[iWantedValue];
  return await iWantedValue;
};

const searchMoreInfo = async (code) => {
  let UsingCode = `&movieCd=${code}`;
  const infoUrl =
    'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json' +
    key +
    UsingCode;
  const responseInfo = await fetch(infoUrl);
  return await responseInfo.json();
};

const ClickedMovieBtn = async (clickedValue) => {
  console.log(clickedValue);
  await showMeTheCode(clickedValue).then((info) => {
    console.log(info);
  });
};
