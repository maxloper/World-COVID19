import React from "react";
import { useLoading, Puff } from "@agney/react-loading";
import "../css/LoadingComponent.css";

const LoadingComponent = () => {
  const { containerProps, indicatorEl } = useLoading({
    loading: true,
    indicator: <Puff width="80" />,
  });

  return (
    <div className="LoadingComponent" {...containerProps}>
      {indicatorEl}
    </div>
  );
};

export default LoadingComponent;
