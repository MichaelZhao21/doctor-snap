import type { NextPage } from "next";

const Home: NextPage = () => {
    return (
        <div
            style={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
                padding: "0 20%",
                height: "100%",
            }}
        >
            <div
                className="card"
                style={{
                    display: "flex",
                    flexDirection: "column",
                    backgroundColor: "white",
                    filter: "drop-shadow(0 0 0.5rem #aaaaaa)",
                    height: "80vh",
                    width: "100%",
                    borderRadius: "1rem",
                    overflow: "hidden",
                    position: "relative",
                }}
            >
                <img
                    style={{
                        width: "100%",
                        objectFit: "cover",
                        height: "20vh",
                        filter: "brightness(70%)",
                    }}
                    src="/medicine.jpg"
                />
                <div
                    style={{
                        position: "absolute",
                        top: "4rem",
                        fontWeight: 800,
                        fontSize: "4rem",
                        color: "white",
                        alignSelf: "center",
                    }}
                >
                    DOCTOR SNAP
                </div>
                <p
                    style={{
                        marginBottom: 0,
                        color: "#777777",
                        marginLeft: "2rem",
                    }}
                >
                    Good morning,
                </p>
                <h1
                    style={{
                        marginTop: "1px",
                        fontSize: "3rem",
                        marginLeft: "2.5rem",
                    }}
                >
                    Johnny Smith
                </h1>
                <div
                    style={{
                        display: "flex",
                        flexDirection: "row",
                        justifyContent: "center",
                        marginBottom: "2rem",
                    }}
                >
                    <div className="inner-card">
                        <div className="ic-sub">Gloves Used this Week</div>
                        <div className="ic-text">10</div>
                    </div>
                    <div className="inner-card">
                        <div className="ic-sub">
                            Minutes Wearing your Current Pair
                        </div>
                        <div className="ic-text">76</div>
                    </div>
                </div>
                <div
                    style={{
                        display: "flex",
                        flexDirection: "row",
                        justifyContent: "center",
                    }}
                >
                    <div className="inner-card">
                        <div className="ic-sub">
                            Carbon Emissions this Week (CO2e)
                        </div>
                        <div className="ic-text">12.5</div>
                    </div>
                    <div className="inner-card">
                        <div className="ic-sub">Cost of Gloves Used</div>
                        <div className="ic-text">$21.93</div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Home;
