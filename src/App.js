import React, { useEffect, useState } from "react";
import axios from "axios";
import "./css/App.css";

// COMPONENTS
import Navigation from "./components/Navigation";
import CountryStats from "./components/CountryStats";
import InfoDetails from "./components/InfoDetails";
import Chart from "./components/Chart";

const App = () => {
  // FETCH COUNTRIES FROM DJANGO API
  useEffect(async () => {
    const { data } = await axios.get("http://127.0.0.1:8000");
    setCountries(data);
    setSearchBar("United States");
  }, []);

  useEffect(async () => {
    const { data } = await axios.get("http://localhost:8000/most-vaccinated/");
    setFetchMostVaccinated(data);
  }, []);

  // SET STATE
  const [countries, setCountries] = useState([]); // Array of objects
  const [searchBar, setSearchBar] = useState(""); // String from Navigation.js Component's <select> value
  const [fetchMostVaccinated, setFetchMostVaccinated] = useState([]); // Array of objects

  // Filter the searched country from Navigation.js component
  const filteredCountry = countries.filter((country) => {
    if (country.country.toLowerCase() === searchBar.toLowerCase()) {
      return country;
    }
  });

  console.log(filteredCountry);

  const handleSearch = (val) => {
    setSearchBar(val);
  };

  return (
    <div className="App">
      <div className="left__screen">
        <Navigation
          countries={countries}
          handleSearch={handleSearch}
          searchBar={searchBar}
          filteredCountry={filteredCountry}
        />
        <CountryStats filteredCountry={filteredCountry} />
        <Chart filteredCountry={filteredCountry} />
      </div>

      <div className="right__screen">
        <InfoDetails
          filteredCountry={filteredCountry}
          fetchMostVaccinated={fetchMostVaccinated}
        />
      </div>
      <div className="circle1"></div>
      <div className="circle2"></div>
      <div className="circle3"></div>
    </div>
  );
};

export default App;
