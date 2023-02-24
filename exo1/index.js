const fs = require('fs');
const csvParser = require('csv-parser');
var counter = 0;
fs.createReadStream('/Users/theorobert/Desktop/scrapping/dc5b_clean_td_ROBERT_Theo/exo1/electronic-card-transactions-december-2022-csv-tables.csv')
.pipe(csvParser())
.on('data', (data) => {
  if (counter < 20) {
    console.log(data);
  }
  counter++;
})
.on('end',()=>{
  console.log('gg')
});