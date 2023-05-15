import ApexCharts from "apexcharts"; 
import { useEffect, useState } from "react";
import read_from_csv from "../data/read";

function Candle(){
  
  useEffect(() => {
    const drawChart = async() => {
      let prices, news = await read_from_csv()
      let options = {
        series: [{
          data: prices
        }],
        chart: {
        type: 'candlestick',
        height: 350,
        events: {
          dataPointSelection: function(event, chartContext, config) {
            let idx = config.dataPointIndex
            let data = news[idx]
            handleClick(data)
            debugger;
            console.log(data)
          }
        }
      },
      title: {
        text: 'CandleStick Chart',
        align: 'left'
      },
      xaxis: {
        type: 'datetime'
      },
      yaxis: {
        tooltip: {
          enabled: true
        }
      }
      };  
      let chart = new ApexCharts(document.querySelector('#chart'), options);
      await chart.render()
    }
    drawChart()
  }, [])

  const [news, setNews] = useState({
    "title": 'Nothing to show',
    "label": 2,
    "date": null,
  });

  const handleClick = (data) => {
    setNews(data)
  }

  return(
    <div>
      <div id="chart">
        <h1>Hello</h1>
      </div>
      <div id='newsBox'>
        <p>{news.title}</p>
        <p>{news.label}</p>
        <p>{news.date == null?'None':news.date.toString()}</p>
      </div>
    </div>
  )
}
export default Candle;