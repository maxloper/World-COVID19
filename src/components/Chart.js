import React from "react";
import { Bar } from "react-chartjs-2";
import "../css/Chart.css";

const Chart = ({ filteredCountry }) => {
  return (
    <>
      {filteredCountry.map((country, i) => {
        return (
          <div className="Chart" key={i}>
            <div className="total_vaccinations_chart">
              <Bar
                key={i}
                data={{
                  labels: ["Total Vaccinations"],
                  datasets: [
                    {
                      data: [country.total_vaccinations],
                      label: `Total Vaccinations in ${country.country}: ${country.total_vaccinations}`,
                      backgroundColor: "#e76f51",
                      borderColor: "#171717",
                      fill: true,
                    },
                  ],
                }}
                height={490}
                width={600}
              />
            </div>
            <div className="daily_vaccinations_chart">
              <Bar
                key={i}
                data={{
                  labels: ["Daily Vaccinations"],
                  datasets: [
                    {
                      data: [country.daily_vaccinations],
                      label: `Daily Vaccinations in ${country.country}: ${country.daily_vaccinations}`,
                      backgroundColor: "#f4a261",
                      borderColor: "#171717",
                      fill: true,
                    },
                  ],
                }}
                height={490}
                width={600}
              />
            </div>
          </div>
        );
      })}
    </>
  );
};

export default Chart;
