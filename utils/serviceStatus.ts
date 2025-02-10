let serviceOpen = true;

export const isServiceOpen = () => serviceOpen;

export const setServiceOpen = (open: boolean) => {
  serviceOpen = open;
};
