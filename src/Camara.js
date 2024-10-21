import React, { useCallback, useRef, useState } from "react";
import Webcam from "react-webcam";

const Camara = () => {
    const webcamRef = useRef(null);
    const [facingMode, setFacingMode] = useState("user");

    const capture = useCallback(() => {
        const imageSrc = webcamRef.current.getScreenshot();
        console.log(imageSrc);
    }, [webcamRef]);

    // Función para alternar entre la cámara frontal y trasera
    const toggleFacingMode = () => {
        setFacingMode(prevMode => (prevMode === "user" ? "environment" : "user"));
    };

    return (
        <div>
            <Webcam
                key={facingMode} // Fuerza la recarga del componente cuando cambia el facingMode
                audio={false}
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                width={400}
                height={400}
                videoConstraints={{ facingMode }}
            />
            <button onClick={capture}>Capturar</button>
            <button onClick={toggleFacingMode}>Cambiar Cámara</button>
        </div>
    );
};

export default Camara;
