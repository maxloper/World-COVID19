import CountUp from "react-countup";
import { Bar } from "react-chartjs-2";
import "../css/InfoDetails.css";

const InfoDetails = ({ filteredCountry, fetchMostVaccinated }) => {
  return (
    <>
      {filteredCountry.length == 0 ? (
        <div className="Details">
          <div className="sources_block">
            <h2>Sources</h2>
            <div className="divider__line"></div>
          </div>
          <div className="most_vaccinated">
            <h2>Most Vaccinated</h2>
          </div>
        </div>
      ) : (
        filteredCountry.map((country, i) => {
          return (
            <div className="Details" key={i}>
              <div className="sources_block">
                <h2>Sources</h2>
                <div className="divider__line"></div>
                <h3>{country.country}</h3>
                <div className="source_links">
                  <a href={country.source_website}>{country.source_name}</a>
                </div>
              </div>

              <div className="most_vaccinated">
                <h2>Most Vaccinated</h2>
                <div className="divider__line"></div>

                {fetchMostVaccinated.map((country, i) => {
                  return (
                    <div key={i}>
                      <h3 id="most_vaccinated">{country.country}</h3>
                      <h2 id="main_result">
                        {
                          <CountUp
                            end={Number(country.total_vaccinations)}
                            duration={1}
                          />
                        }
                      </h2>
                      <Bar
                        key={i}
                        data={{
                          labels: ["Total Vaccinations"],
                          datasets: [
                            {
                              data: [country.total_vaccinations],
                              label: `Total Vaccinations: ${country.total_vaccinations}`,
                              backgroundColor: "#e9c46a",
                              borderColor: "#171717",
                              fill: true,
                            },
                          ],
                        }}
                        height={290}
                        width={290}
                      />
                    </div>
                  );
                })}
              </div>
            </div>
          );
        })
      )}
    </>
  );
};

export default InfoDetails;
