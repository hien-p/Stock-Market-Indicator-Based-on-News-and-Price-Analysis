
async function read_from_csv(path = './src/data/tmp_vib.json'){
    const keys = ['Date','Highest','Open','Closed','Lowest','title','pred']
    const fs = new FileReader()
    
    const content = await fs.readFile(path, { encoding: 'utf8' });
    let data = JSON.parse(content)
    let prices = {}
    let result = []
    let news = []
    keys.forEach(e => prices[e] = Object.values(data[e])) 
    for(let i=0; i < prices['Date'].length; ++i){
        let Y = ['Highest','Open','Closed','Lowest'].map(e => prices[e][i])
        let X = new Date(prices['Date'][i])
        result.push({x: X, y: Y})
        news.push({title: prices['title'][i], label: prices['pred'][i]})
    }
    console.log(result, news)
    return result, news
}

export default read_from_csv