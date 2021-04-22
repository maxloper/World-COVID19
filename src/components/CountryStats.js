import React from "react";
import LoadingComponent from "./LoadingComponent";
import CountUp from "react-countup";
import "../css/CountryStats.css";

const CountryStats = ({ filteredCountry }) => {
  return (
    <>
      {filteredCountry.length == 0 ? (
        <LoadingComponent />
      ) : (
        filteredCountry.map((country, i) => {
          return (
            <div className="Stats" key={i}>
              <div className="total_vaccinations">
                <h3>Total Vaccinations</h3>
                <div className="divider__line"></div>
                <p>{country.country}</p>
                <p id="date">{new Date(country.date).toDateString()}</p>
                <h2 id="main_result">
                  <CountUp
                    end={Number(country.total_vaccinations)}
                    duration={1}
                  />
                </h2>
              </div>
              <div className="daily_vaccinations">
                <h3>Daily Vaccinations</h3>
                <div className="divider__line"></div>
                <p>{country.country}</p>
                <p id="date">{new Date(country.date).toDateString()}</p>
                <h2 id="main_result">
                  <CountUp
                    end={Number(country.daily_vaccinations)}
                    duration={1}
                  />
                </h2>
              </div>
              <div className="vaccines">
                <h3>Vaccine Used</h3>
                <div className="divider__line"></div>
                <p>{country.country}</p>
                <p id="date">{new Date(country.date).toDateString()}</p>
                <h2 id="vaccine_main_result">{country.vaccines}</h2>
              </div>
            </div>
          );
        })
      )}
    </>
  );
};

export default CountryStats;
