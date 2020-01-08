/*
 * Container component
 * All data handling & manipulation should be handled here.
 */

import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

import OrganizationDetailsPage from './components/OrganizationDetailsPage';

const OrganizationDetailsContainer = (props) => {
  const [details, setDetails] = useState({});
  const [loading, setLoading] = useState(true);
  const { keycloak } = props;

  const refreshDetails = () => {
    const { token } = keycloak;

    setLoading(true);

    axios.get('http://localhost/api/users/current', {
      headers: { Authorization: `Bearer ${token}` },
    }).then((response) => {
      const { organization, displayName } = response.data;

      setDetails({
        displayName,
        organization,
      });

      setLoading(false);
    });
  };

  useEffect(() => {
    refreshDetails();
  }, [keycloak.authenticated]);

  return (
    <OrganizationDetailsPage
      details={details}
      loading={loading}
    />
  );
};

OrganizationDetailsContainer.propTypes = {
  keycloak: PropTypes.shape().isRequired,
};

export default OrganizationDetailsContainer;
