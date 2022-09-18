import type { NextPage } from "next";
import { useState } from "react";

const Home: NextPage = () => {
    const [num, setNum] = useState(10);
    const [mins, setMins] = useState(90.4);

    const increment = () => {
        setNum(num + 1);
        setMins(Math.random() * 20 + 80);
    };

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
            <button
                style={{
                    position: "fixed",
                    bottom: "2rem",
                    right: "2rem",
                    borderRadius: "100rem",
                    border: "none",
                    fontSize: "3rem",
                    fontWeight: "700",
                    width: "4rem",
                    height: "4rem",
                    filter: "drop-shadow(0 0 0.2rem #aaaaaa)",
                    transition: "0.2s",
                    cursor: "pointer",
                }}
                onClick={increment}
            >
                +
            </button>
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
                    className="title"
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
                        <div className="ic-text">{num}</div>
                    </div>
                    <div className="inner-card">
                        <div className="ic-sub">
                            Minutes Wearing your Current Pair
                        </div>
                        <div className="ic-text">{mins.toFixed(1)}</div>
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
                            Carbon Emissions this Week (kg CO2e)
                        </div>
                        <div className="ic-text">{(num * 0.21).toFixed(3)}</div>
                    </div>
                    <div className="inner-card">
                        <div className="ic-sub">Cost of Gloves Used</div>
                        <div className="ic-text">
                            ${(num * 0.15).toFixed(2)}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Home;
