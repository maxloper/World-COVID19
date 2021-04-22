import React from "react";
import "../css/Navigation.css";

const Navigation = ({ handleSearch, searchBar, countries }) => {
  const handleSearchResult = (e) => {
    handleSearch(e.target.value);
  };
  return (
    <div className="NavigationComponent">
      <div className="main__title">
        <h1>COVID-19</h1>
        <h1>World Vaccinations</h1>
      </div>
      <div className="navbar__search">
        <form>
          <h2>Search Country</h2>

          <select
            name="countries"
            id="select-country"
            onChange={handleSearchResult}
            value={searchBar}
          >
            <option value="United States">United States</option>
            {countries.map((country, i) => (
              <option value={country.country} key={i}>
                {country.country}
              </option>
            ))}
          </select>
        </form>
      </div>
    </div>
  );
};

export default Navigation;
