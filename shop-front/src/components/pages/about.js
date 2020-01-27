import React from "react";
import profilePicture from "../../../static/assets/images/donuts.jpg";

export default function() {
  return (
    <div className="content-page-wrapper">
      <div
        className="left-column"
        style={{
          background: "url(" + profilePicture + ") no-repeat",
          backgroundSize: "cover",
          backgroundPosition: "center"
        }}
      />
      <div className="right-column">
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam eum
          magni incidunt fugiat quaerat quas rerum reiciendis? Praesentium
          repellat corporis mollitia tempore eum illum, ipsum, natus explicabo
          aperiam incidunt perspiciatis corrupti quasi? Nesciunt quibusdam sint
          tenetur nam quaerat officia, repellat reprehenderit, nulla harum, illo
          sequi nihil omnis quae inventore asperiores.
        </p>
      </div>
    </div>
  );
}
